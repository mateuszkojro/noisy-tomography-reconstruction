import dxchange
import h5py
import matplotlib.pyplot as plt
import numpy as np
import tomopy

proj, flat, dark, theta = dxchange.read_aps_32id("data/tomo_00031.h5")

proj = tomopy.normalize(proj, flat, dark)

proj = tomopy.remove_stripe_fw(proj)

proj = tomopy.minus_log(proj)

recon = tomopy.recon(proj, theta, center=484.5, algorithm="gridrec")

recon = tomopy.circ_mask(recon, axis=0, ratio=0.95)

dxchange.write_tiff_stack(recon, fname="recon/recon")

img = recon[recon.shape[0] // 2]

plt.imshow(
    img,
    vmin=np.percentile(img, 1),
    vmax=np.percentile(img, 99),
)
plt.colorbar()
plt.show()
