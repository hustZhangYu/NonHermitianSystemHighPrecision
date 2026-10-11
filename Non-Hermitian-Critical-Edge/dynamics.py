"""Shared dynamics primitives; preserve the legacy time grid and observables."""
import mpmath as mp

def initial_state(L):
#  construct an initial state with given system size
    psi=mp.zeros(L,1)
    psi[mp.floor(L/2),0]=1
    return psi

def time_evolution_renormalization(H,psi,T,dt):
#   Calculate the time evolution of the initial state under the Non-Hermitian Physics
#   we renormalize the wavefunction after a time interval
#   parameters: H:Hamiltonian, psi: initial state, T: all time, dt: time interval 
    
    # prepartion 
    L=len(psi)
    psit=psi
    Data=list()
    XmeanData=list()
    psit2=list()
    Xmean=0
    count=-L/2
    for m in psit:
        psit2.append(mp.re(m*mp.conj(m)))
        Xmean=Xmean+mp.re(m*mp.conj(m))*(count*count)
        count=count+1
    Data.append(psit2)
    XmeanData.append(Xmean)

    # unitary operator
    U=mp.expm(-1j*H*dt)
    t=0
    while t+dt<T:
        psit=U@psit
        s=0
        for m in psit:
            s=s+m*mp.conj(m)
        psit2=list()
        Xmean=0
        count=-L/2
        for m in psit:
            psit2.append(mp.re(m*mp.conj(m)/s))
            Xmean=Xmean+mp.re(m*mp.conj(m)/s)*(count*count)
            count=count+1
        Data.append(psit2)
        XmeanData.append(Xmean)
        t=t+dt
    return Data, XmeanData, psit2
