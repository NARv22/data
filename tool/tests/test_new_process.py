import os
import time
from core.configuration.consts import (
    PATH_TO_MARABOU_APPLICATIONS_ACAS_EXAMPLES, VERBOSE
)
from core.pre_process.pre_process import preprocess, preprocess_split_pos_neg
from core.pre_process.pre_process_mine import do_process_after, do_process_before
from core.nnet.read_nnet import network_from_nnet_file
from core.data_structures.Network import Network
from core.data_structures.Layer import Layer
from core.data_structures.ARNode import ARNode
from core.data_structures.Edge import Edge
from core.utils.verification_properties_utils import TEST_PROPERTY_ACAS

def test_process():
    nnet_dir = PATH_TO_MARABOU_APPLICATIONS_ACAS_EXAMPLES
    filename = "ACASXU_run2a_2_2_batch_2000.nnet"
    #nnet_filename = "testnet.nnet"
    nnet_filename = os.path.join(nnet_dir, filename)
    net = network_from_nnet_file(nnet_filename)
    #print(net)
    t1 = time.time()
    test_property = TEST_PROPERTY_ACAS["basic_1"]
    do_process_before(net,test_property)
    #print(net)
    t2 = time.time()
    #do_process_after(net)
    t3 = time.time()
    preprocess(net)
    do_process_after(net)
    t4 = time.time()
    nodes2variables, variables2nodes = net.get_variables()
    print(nodes2variables)
    print(variables2nodes)
    
    print("区间计算时间"+str(t2-t1))
    print("分裂节点时间"+str(t3-t2))
    print("删除节点时间"+str(t4-t3))
    #print(net)
if __name__ == '__main__':
    test_process()