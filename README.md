# Nanoelectronic Circuit Design

## Compile and run
```bash
ngspice
cd [path_to_source_spi_files]
source run_nand2.spi
run
write nand2_out.raw
Spice x -> quit
```

## Plot waves
```bash
ngspice
cd [path_to_source_spi_files]
source run_nand2.spi
run
display
plot signal1 signal2 signal3
```