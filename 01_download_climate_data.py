import requests
import os

# List of URLs to download
urls = [
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_01_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_02_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_03_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_04_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_05_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_06_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_07_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_08_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_09_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_10_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_11_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_12_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_01_2011_2040_norm.tif",
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_02_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_03_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_04_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_05_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_06_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_07_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_08_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_09_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_10_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_11_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_12_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_01_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_02_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_03_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_04_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_05_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_06_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_07_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_08_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_09_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_10_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_11_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2011-2040/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_12_2011_2040_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_01_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_02_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_03_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_04_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_05_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_06_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_07_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_08_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_09_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_10_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_11_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_12_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_01_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_02_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_03_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_04_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_05_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_06_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_07_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_08_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_09_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_10_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_11_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_12_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_01_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_02_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_03_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_04_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_05_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_06_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_07_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_08_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_09_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_10_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_11_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2041-2070/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_12_2041_2070_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_01_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_02_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_03_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_04_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_05_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_06_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_07_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_08_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_09_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_10_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_11_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tas/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tas_12_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_01_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_02_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_03_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_04_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_05_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_06_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_07_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_08_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_09_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_10_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_11_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmax/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmax_12_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_01_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_02_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_03_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_04_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_05_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_06_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_07_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_08_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_09_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_10_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_11_2071_2100_norm.tif", 
"https://os.zhdk.cloud.switch.ch/chelsav2/GLOBAL/climatologies/2071-2100/MPI-ESM1-2-HR/ssp126/tasmin/CHELSA_mpi-esm1-2-hr_r1i1p1f1_w5e5_ssp126_tasmin_12_2071_2100_norm.tif"
]


# Directory to save the downloaded files
output_dir = "input"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to download a single file
def download_file(url):
    local_filename = os.path.join(output_dir, url.split("/")[-1])
    # Send the GET request
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Check for errors
        # Write the content in chunks to avoid memory overload
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    return local_filename

# Download all files
for url in urls:
    try:
        print(f"Downloading {url}...")
        download_file(url)
        print(f"Downloaded {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
