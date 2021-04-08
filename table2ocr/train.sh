onmt_train -model_type img \
           -data demo \
           -save_model demo-model \
           -gpu_ranks 0 \
           -batch_size 20 \
           -max_grad_norm 20 \
           -learning_rate 0.1 \
           -word_vec_size 80 \
           -encoder_type brnn \
           -image_channel_size 1