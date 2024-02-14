docker run -w $PWD -v <MOUNT_DIR>:<MOUNT_DIR> quay.io/singlecellpipeline/wgs_breakpoint:v0.2.4 wgs breakpoint_calling \
    --input_yaml input.yaml --out_dir results --loglevel DEBUG --submit local --maxjobs 24  --refdir <WGS-GRCh38_DIR> --sentinel_only --nocleanup
