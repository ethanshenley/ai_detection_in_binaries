from typing import Dict, List, Any
import json
import networkx as nx
from pathlib import Path

class VisualizationUtils:
    """Utilities for generating visualization data."""
    
    @staticmethod
    def cfg_to_d3_format(cfg: nx.DiGraph) -> Dict[str, Any]:
        """
        Convert NetworkX CFG to D3.js compatible format.
        
        Args:
            cfg: NetworkX directed graph representing CFG
            
        Returns:
            Dictionary with nodes and links in D3.js format
        """
        nodes = []
        links = []
        
        # Create node mapping for index-based references
        node_map = {node: idx for idx, node in enumerate(cfg.nodes())}
        
        # Add nodes
        for node in cfg.nodes():
            nodes.append({
                "id": node_map[node],
                "address": hex(node) if isinstance(node, int) else str(node),
                "type": cfg.nodes[node].get('type', 'basic_block'),
                "size": len(cfg.nodes[node].get('instructions', [])),
            })
        
        # Add links
        for source, target in cfg.edges():
            links.append({
                "source": node_map[source],
                "target": node_map[target],
                "type": cfg.edges[source, target].get('type', 'flow')
            })
        
        return {
            "nodes": nodes,
            "links": links
        }
    
    @staticmethod
    def generate_confidence_chart(scores: Dict[str, float]) -> Dict[str, Any]:
        """
        Generate chart data for framework detection confidence scores.
        
        Args:
            scores: Dictionary of framework names and confidence scores
            
        Returns:
            Dictionary with chart configuration
        """
        return {
            "type": "bar",
            "data": [
                {"framework": k, "confidence": v * 100}
                for k, v in scores.items()
            ],
            "config": {
                "xAxis": "framework",
                "yAxis": "confidence",
                "yFormat": ".1f"
            }
        }
    
    @staticmethod
    def save_visualization(data: Dict[str, Any], output_path: str) -> None:
        """
        Save visualization data to JSON file.
        
        Args:
            data: Visualization data
            output_path: Path to save JSON file
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
            
    @staticmethod
    def tensor_ops_heatmap(
        tensor_ops: Dict[str, List[tuple]], 
        binary_size: int
    ) -> Dict[str, Any]:
        """
        Generate heatmap data for tensor operations locations.
        
        Args:
            tensor_ops: Dictionary of operation types and their locations
            binary_size: Total size of the binary
            
        Returns:
            Dictionary with heatmap configuration
        """
        # Create bins for heatmap
        num_bins = 50
        bin_size = binary_size / num_bins
        
        heatmap_data = []
        for op_type, locations in tensor_ops.items():
            bins = [0] * num_bins
            for addr, size in locations:
                bin_idx = min(int(addr / bin_size), num_bins - 1)
                bins[bin_idx] += 1
                
            heatmap_data.append({
                "operation": op_type,
                "distribution": bins
            })
        
        return {
            "type": "heatmap",
            "data": heatmap_data,
            "config": {
                "xAxis": "binary_location",
                "yAxis": "operation_type",
                "binSize": bin_size,
                "totalBins": num_bins
            }
        }