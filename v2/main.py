import model
import tensorflow as tf

if __name__ == '__main__':
    train = False
    if train:
        with tf.Session() as sess:
            lstmRNN = model.LstmRNN(sess)
            lstmRNN.fit()
            #sess.run(lstmRNN.cell_output.shape)
    else:
        with tf.Session() as sess:
            lstmRNN = model.LstmRNN(sess)
            #lstmRNN.predict(['0050','0051','0052','0053','0054','0055','0056','0057','0058','0059','006201',
            #                '006203','006204','006208','00690','00692','00701','00713'],['20180501']*18)
            stockNo = ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '6201',
                       '6203', '6204', '6208', '690', '692', '701', '713']
            dates = ['20180525', '20180518', '20180427', '20180420', '20180413',
                '20180330', '20180323', '20180316', '20180309', '20180302', '20180223', '20180209', '20180202', '20180126', '20180119', '20180112']
            dates3 = ['20180110', '20180111', '20180112', '20180115', '20180116', '20180117', '20180118', '20180119', '20180122', '20180123', '20180124', '20180125', '20180126', '20180129', '20180130', '20180131', '20180201', '20180202', '20180205', '20180206', '20180207', '20180208', '20180209', '20180212', '20180221', '20180222', '20180223', '20180226', '20180227', '20180301', '20180302', '20180305', '20180306', '20180307', '20180308', '20180309', '20180312', '20180313', '20180314', '20180315', '20180316', '20180319', '20180320', '20180321', '20180322', '20180323', '20180326', '20180327', '20180328', '20180329', '20180330', '20180331', '20180402', '20180403', '20180409', '20180410', '20180411', '20180412', '20180413', '20180416', '20180417', '20180418', '20180419', '20180420', '20180423', '20180424', '20180425', '20180426', '20180427', '20180430', '20180502', '20180503', '20180504', '20180507', '20180508', '20180509', '20180510', '20180511', '20180514', '20180515', '20180516', '20180517', '20180518', '20180521', '20180522', '20180523', '20180524', '20180525', '20180528', '20180529', '20180530', '20180531', '20180601', '20180604', '20180605', '20180606', '20180607', '20180608']
            dates2 = ['20180611', '20180612', '20180613', '20180614', '20180615']
            for date in dates2:
                lstmRNN.predict(stockNo, date)