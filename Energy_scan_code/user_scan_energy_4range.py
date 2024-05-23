from scan_energy_range import scan_energy_4_ranges
#scan_energy_4_ranges(1st_start_energy, E step size, num of E points, 2nd_start_energy, E step size, num of E points, 3rd_start_energy,  E step size, num of E points, 4th_start_energy,  E step size, num of E points, file_name="test.txt", exposure_time=0.05)
scan_energy_4_ranges(8000, 5, 6, 8051, 1, 6, 8110, 10, 6, 8280, 10, 6, off_sample=8,file_name="test.txt", exposure_time=0.05)
        
