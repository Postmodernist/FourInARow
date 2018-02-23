import tensorflow as tf


def softmax_cross_entropy_with_logits(y_true, y_predicted):
    pi = y_true
    p = y_predicted
    zero = tf.zeros(shape=tf.shape(pi), dtype=tf.float32)
    where = tf.equal(pi, zero)
    negatives = tf.fill(tf.shape(pi), -100.0)
    p = tf.where(where, negatives, p)
    return tf.nn.softmax_cross_entropy_with_logits_v2(labels=pi, logits=p)
