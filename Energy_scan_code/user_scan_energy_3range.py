from scan_energy_range import scan_energy_3_ranges 
#scan_energy_4_ranges(1st_start_energy, E step size, num of E points, 2nd_start_energy, E step size, num of E points, 3rd_start_energy,  E step size, num of E points, 4th_start_energy,  E step size, num of E points, file_name="test.txt", exposure_time=0.05)
scan_energy_3_ranges(8000, 5, 5, 8051, 1, 5, 8110, 10, 5, off_sample=8, file_name="test.txt", exposure_time=0.05)
        
