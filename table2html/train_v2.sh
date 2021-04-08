onmt_train -model_type img \
           -data demo \
           -save_model demo-v2-model \
           -gpu_ranks 0 \
           -batch_size 20 \
           -max_grad_norm 20 \
           -learning_rate 0.1 \
           -word_vec_size 3000 \
           -encoder_type cnn \
           -image_channel_size 1