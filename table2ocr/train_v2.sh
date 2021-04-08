onmt_train -model_type img \
           -data demo \
           -save_model demo-v2-model \
           -gpu_ranks 0 \
           -batch_size 30 \
           -max_grad_norm 20 \
           -learning_rate 0.1 \
           -word_vec_size 3000 \
           -encoder_type cnn \
           -image_channel_size 1 \
           --log_file 0202.lz.log \
           --label_smoothing 0.1 \
           --train_step 10000000 \
           --rnn_type LSTM

