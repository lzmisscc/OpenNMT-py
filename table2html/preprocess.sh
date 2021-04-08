onmt_preprocess -data_type img \
                -src_dir images/ \
                -train_src src-train.txt \
                -train_tgt tgt-train.txt -valid_src src-val.txt \
                -valid_tgt tgt-val.txt -save_data demo \
                -tgt_seq_length 3000 \
                -tgt_words_min_frequency 2 \
                -shard_size 50000 \
                -image_channel_size 1 \
                -overwrite