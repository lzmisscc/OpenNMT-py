onmt_translate -data_type img \
               -model demo-v2-model_step_700000.pt \
               -src_dir data_v2 \
               -src src-test \
               -output pred_v2.txt \
               -max_length 3000 \
               -beam_size 5 \
               -gpu 0 \
                -image_channel_size 1 \
                -batch_size 1 \
                -report_time \
               -verbose 
                #           --label_smoothing 0.1 \
                # --rnn_type LSTM

# model_step_95000