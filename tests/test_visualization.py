import pytest
import networkx as nx
from src.utils.visualization import VisualizationUtils

def test_cfg_to_d3_format():
    # Create a simple CFG
    cfg = nx.DiGraph()
    cfg.add_node(0x1000, instructions=['mov eax, 1'])
    cfg.add_node(0x1010, instructions=['ret'])
    cfg.add_edge(0x1000, 0x1010)
    
    d3_data = VisualizationUtils.cfg_to_d3_format(cfg)
    
    assert 'nodes' in d3_data
    assert 'links' in d3_data
    assert len(d3_data['nodes']) == 2
    assert len(d3_data['links']) == 1
    assert d3_data['nodes'][0]['address'] == '0x1000'
    
def test_generate_confidence_chart():
    scores = {
        'tensorflow': 0.8,
        'pytorch': 0.2,
        'unknown': 0.0
    }
    
    chart_data = VisualizationUtils.generate_confidence_chart(scores)
    
    assert chart_data['type'] == 'bar'
    assert len(chart_data['data']) == 3
    assert chart_data['data'][0]['confidence'] == 80.0
    
def test_tensor_ops_heatmap():
    tensor_ops = {
        'matmul': [(0x1000, 10), (0x2000, 15)],
        'conv': [(0x1500, 20)]
    }
    binary_size = 0x3000
    
    heatmap_data = VisualizationUtils.tensor_ops_heatmap(tensor_ops, binary_size)
    
    assert heatmap_data['type'] == 'heatmap'
    assert len(heatmap_data['data']) == 2
    assert all(len(op['distribution']) == 50 for op in heatmap_data['data'])
    
def test_save_visualization(tmp_path):
    test_data = {"test": "data"}
    output_path = tmp_path / "viz" / "test.json"
    
    VisualizationUtils.save_visualization(test_data, str(output_path))
    
    assert output_path.exists()
    with open(output_path) as f:
        saved_data = f.read()
        assert '"test": "data"' in saved_data