import pytest
import random
from src.lzss_compression import LZSSCompressor

def test_lzss_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZSSCompressor()
    test_data = b"Hello, hello, hello world!"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_empty_data():
    """Test compression and decompression of empty data"""
    compressor = LZSSCompressor()
    test_data = b""
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_repeated_patterns():
    """Test compression of data with repeated patterns"""
    compressor = LZSSCompressor()
    test_data = b"ABCABCABCABCABCABC"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_random_data():
    """Test compression of random data"""
    compressor = LZSSCompressor()
    test_data = bytes(random.getrandbits(8) for _ in range(1000))
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_custom_parameters():
    """Test compression with custom window size and min match length"""
    compressor = LZSSCompressor(window_size=128, min_match_length=4)
    test_data = b"Hello, hello, hello world! Repeated patterns are good for compression."
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_string_input():
    """Test compression with string input"""
    compressor = LZSSCompressor()
    test_data = "Hello, hello, hello world!"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data.encode('utf-8')

def test_invalid_marker_raises_error():
    """Test that invalid marker bytes raise an error during decompression"""
    compressor = LZSSCompressor()
    invalid_compressed_data = b'\x02'  # Invalid marker byte
    
    with pytest.raises(ValueError):
        compressor.decompress(invalid_compressed_data)