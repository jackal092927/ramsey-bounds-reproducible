"""Numerical check of the Schur-complement filling bound
   Delta_up >= (||v||^2/||c(lambda)||^2) |v><v|/||v||^2 ,  v = d c(lambda),
for the certified atoms, and the scaling of the optimal constant 1/<v,(Delta_up)^+ v>."""
import json, itertools, os, numpy as np
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"manuscript_v0","supplement"))
from numpy.linalg import eigvalsh, pinv, norm

def load_atom(kind):
    if kind=="rep":
        d=json.load(open("RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json"))
        verts=[str(v) for v in d["graph"]["vertices"]]; edges=[tuple(map(str,e)) for e in d["graph"]["edges"]]
        reg=set(map(str,d["zero_weight_certificate"]["register_vertices"])); fill=d["topology_certificate"]["exact_filling_chain"]; deg=3
    else:
        r=json.load(open("REMAINING_ACTIVE_ATOM_CERTIFICATES.json"))["atoms"][kind]
        verts=[str(v) for v in r["graph"]["vertices"]]; edges=[tuple(map(str,e)) for e in r["graph"]["edges"]]
        reg=set(map(str,r["zero_weight_certificate"]["register_vertices"])); fill=r["topology_certificate"]["exact_filling_chain"]; deg=r["topology_certificate"]["target_degree"]
    return verts,edges,reg,fill,deg

def cliques(verts,edges,k):
    adj={v:set() for v in verts}
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    order={v:i for i,v in enumerate(verts)}
    out=[]
    def ext(cl,cands):
        if len(cl)==k+1: out.append(tuple(cl)); return
        for v in sorted(cands,key=lambda x:order[x]):
            if all(order[v]>order[u] for u in cl):
                ext(cl+[v],cands & adj[v])
    for v in verts: ext([v],adj[v])
    return sorted(out,key=lambda s:[order[x] for x in s])

def boundary(simp_k,simp_km1,weights):
    rows={s:i for i,s in enumerate(simp_km1)}
    B=np.zeros((len(simp_km1),len(simp_k)))
    for j,s in enumerate(simp_k):
        for i,v in enumerate(s):
            B[rows[s[:i]+s[i+1:]],j]=(-1)**i*weights[v]
    return B

for kind in ["state_0m1","state_00m11","rep"]:
    verts,edges,reg,fill,deg=load_atom(kind)
    Sd=cliques(verts,edges,deg); Sd1=cliques(verts,edges,deg+1)
    idx={s:j for j,s in enumerate(Sd1)}
    order={v:i for i,v in enumerate(verts)}
    # integer filling as a vector on (deg+1)-simplices with orientation sign
    c1=np.zeros(len(Sd1))
    for term in fill:
        s=[str(v) for v in term["simplex"]]
        srt=tuple(sorted(s,key=lambda x:order[x]))
        # sign of permutation from given order to sorted order
        perm=[srt.index(v) for v in s]
        sign=1
        for i in range(len(perm)):
            for j in range(i+1,len(perm)):
                if perm[i]>perm[j]: sign=-sign
        c1[idx[srt]]+=sign*term["coefficient"]
    priv=lambda s: sum(1 for v in s if v not in reg)
    p=max(priv(s) for s in Sd1 if c1[idx[s]]!=0)
    print(f"== {kind}: deg={deg}, #d-simplices={len(Sd)}, #(d+1)={len(Sd1)}, filling depth p={p}")
    for lam in [0.5,0.25,0.125,0.0625]:
        w={v:(1.0 if v in reg else lam) for v in verts}
        B=boundary(Sd1,Sd,w)                       # weighted d+1 boundary
        Wd1=np.array([np.prod([w[v] for v in s]) for s in Sd1])
        c=c1/Wd1                                   # weighted filling W^{-1} c1
        v=B@c
        assert norm(v[[i for i,s in enumerate(Sd) if priv(s)>0]])<1e-9, "v not a register chain"
        up=B@B.T
        vhat=v/norm(v)
        bound=norm(v)**2/norm(c)**2               # Schur-complement constant
        opt=1.0/(vhat@pinv(up,rcond=1e-12)@vhat)   # optimal constant
        minev=eigvalsh(up-bound*np.outer(vhat,vhat))[0]
        print(f"  lam={lam:8.5f}  bound={bound:.3e}  optimal={opt:.3e}  min eig(up - bound*P)={minev:.2e}  bound/lam^(2p)={bound/lam**(2*p):.3f}  opt/lam^(2p)={opt/lam**(2*p):.3f}")
