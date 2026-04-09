import numpy as np
import matplotlib.pyplot as plt

# UniNet parameters
A_cong     = 0.21303810070914728
tau_relax  = 1.1476764518546496
lambda_DM  = 1.0797405752016858
Phi_ratio  = 63.66871384426313

# Grid (flat-sky patch)
N = 1024
L = 10.0  # degrees across (arbitrary)
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
kx = np.fft.fftfreq(N, d=(x[1]-x[0])) * 2*np.pi
ky = np.fft.fftfreq(N, d=(y[1]-y[0])) * 2*np.pi
KX, KY = np.meshgrid(kx, ky)
ell = np.sqrt(KX**2 + KY**2)

# UniNet-style transfer function in 2D k-space
def uninet_transfer_2d(ell):
    # map |k| to an effective ell-like scale
    # (just a toy identification)
    ell_eff = ell

    damping   = np.exp(-(ell_eff / (1500 / tau_relax))**2)
    coupling  = 1 + lambda_DM * np.exp(-ell_eff / 200)
    potential = Phi_ratio / (1 + (ell_eff / 20)**2)

    return A_cong * coupling * potential * damping

T_k = uninet_transfer_2d(ell)

# Random phases, Gaussian amplitudes
np.random.seed(123)
phase = np.random.uniform(0, 2*np.pi, size=ell.shape)
amp   = np.random.normal(size=ell.shape)

# Complex field in k-space
field_k = amp * np.exp(1j * phase) * T_k

# Back to real space
field = np.fft.ifft2(field_k).real

# Normalize for nicer contrast
field = (field - field.mean()) / field.std()

# Plot
plt.figure(figsize=(8, 4))
plt.imshow(field, cmap="coolwarm", origin="lower",
           extent=[-L/2, L/2, -L/2, L/2])
plt.colorbar(label="ΔT (arb. units)")
plt.title("Toy UniNet-style CMB Patch (Flat Sky)")
plt.xlabel("x [deg]")
plt.ylabel("y [deg]")
plt.tight_layout()
plt.savefig("uninet_cmb_patch.png", dpi=200)