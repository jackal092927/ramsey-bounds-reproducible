"""Harmonic concentration check on the real |0>-|1> atom:
X_in = one bowtie register (H_in = V, dim 2), X_out = X_in + state_0m1 gadget (K_out = span|+>, dim 1).
Compute sin(theta) between the surviving harmonic vector of X_out and V, versus lambda."""
import json, itertools, numpy as np
from numpy.linalg import svd, norm
from scipy.linalg import eigh, null_space
import os; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"manuscript_v0","supplement"))
r=json.load(open("REMAINING_ACTIVE_ATOM_CERTIFICATES.json"))["atoms"]["state_0m1"]
verts=[str(v) for v in r["graph"]["vertices"]]; edges=[tuple(map(str,e)) for e in r["graph"]["edges"]]
reg=set(map(str,r["zero_weight_certificate"]["register_vertices"]))
order={v:i for i,v in enumerate(verts)}
adj={v:set() for v in verts}
for a,b in edges: adj[a].add(b); adj[b].add(a)
def cliques(vs,k):
    out=[]
    def ext(cl,c):
        if len(cl)==k+1: out.append(tuple(cl)); return
        for v in sorted(c,key=lambda x:order[x]):
            if all(order[v]>order[u] for u in cl): ext(cl+[v],c&adj[v])
    for v in vs: ext([v],adj[v]&set(vs))
    return sorted(out,key=lambda s:[order[x] for x in s])
def boundary(sk,skm1,w):
    rows={s:i for i,s in enumerate(skm1)}; B=np.zeros((len(skm1),len(sk)))
    for j,s in enumerate(sk):
        for i,v in enumerate(s): B[rows[s[:i]+s[i+1:]],j]=(-1)**i*w[v]
    return B
def harmonic(vs,d,w):
    Sd=cliques(vs,d); Sdm=cliques(vs,d-1); Sdp=cliques(vs,d+1)
    down=boundary(Sd,Sdm,w); up=boundary(Sdp,Sd,w) if Sdp else np.zeros((len(Sd),0))
    lap=down.T@down+up@up.T
    ev,vec=eigh(lap); H=vec[:,np.abs(ev)<1e-10]; gap=ev[ev>1e-10][0] if np.any(ev>1e-10) else None
    return Sd,H,gap
regv=sorted(reg,key=lambda x:order[x])
Sd_in,H_in,_=harmonic(regv,1,{v:1.0 for v in verts})   # register only: V (2-dim), unweighted
print("dim V =",H_in.shape[1])
for lam in [0.5,0.25,0.125,0.0625,0.03125]:
    w={v:(1.0 if v in reg else lam) for v in verts}
    Sd_out,H_out,gap=harmonic(verts,1,w)
    # embed V into C_1(X_out)
    idx={s:i for i,s in enumerate(Sd_out)}
    E=np.zeros((len(Sd_out),len(Sd_in)))
    for j,s in enumerate(Sd_in): E[idx[s],j]=1
    Vemb=E@H_in
    sv=svd(H_out.T@Vemb,compute_uv=False)   # singular values of P_Hout restricted to V (2 values; rank should be 1)
    # distance of the harmonic vector to V
    h=H_out[:,0]; dist=norm(h-Vemb@(Vemb.T@h))
    print(f"lam={lam:8.5f} dim H_out={H_out.shape[1]} gap={gap:.3e} singular values of P_Hout|V={np.round(sv,6)} ||(I-P_V)h||={dist:.3e} ratio dist/lam={dist/lam:.3f}")
