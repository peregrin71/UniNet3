import numpy as np
import healpy as hp

# -----------------------------
# 1. Your inferred parameters
# -----------------------------
A_cong     = 0.21303810070914728
tau_relax  = 1.1476764518546496
lambda_DM  = 1.0797405752016858
Phi_ratio  = 63.66871384426313

# -----------------------------
# 2. Define a simple UniNet transfer function
# -----------------------------
def uninet_transfer(ell):
    # Congestion smoothing (Silk-like)
    damping = np.exp(-(ell / (1500 / tau_relax))**2)

    # Matter coupling (affects peak contrast)
    coupling = 1 + lambda_DM * np.exp(-ell / 200)

    # Potential modulation (large-scale power)
    potential = Phi_ratio / (1 + (ell / 20)**2)

    # Combine
    return A_cong * coupling * potential * damping

# -----------------------------
# 3. Build a toy power spectrum
# -----------------------------
lmax = 2048
ells = np.arange(lmax + 1)
Cl = uninet_transfer(ells)

# Ensure positivity
Cl = np.abs(Cl)

# -----------------------------
# 4. Generate a random sky map
# -----------------------------
nside = 256
sky = hp.synfast(Cl, nside=nside, verbose=False)

# -----------------------------
# 5. Visualize
# -----------------------------
hp.mollview(sky, title="Simulated UniNet CMB Sky")
hp.graticule()
