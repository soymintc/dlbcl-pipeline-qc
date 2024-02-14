singularity run -B <MOUNT_DIR> docker://quay.io/wgspipeline/wgs_breakpoint:v0.2.4 wgs breakpoint_calling \
    --input_yaml inputs.yaml --out_dir results --submit local --maxjobs 24 --refdir <WGS-GRCh38_REF_DIR> --sentinel_only --nocleanup
