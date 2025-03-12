class LZSSCompressor:
    """
    Implements the Lempel-Ziv-Storer-Szymanski (LZSS) compression algorithm.
    
    The algorithm replaces repeated sequences with references to their previous occurrences,
    reducing the overall data size by encoding repeated patterns more efficiently.
    """
    
    def __init__(self, window_size=4096, min_match_length=3):
        """
        Initialize the LZSS compressor.
        
        :param window_size: Size of the sliding window for searching previous matches
        :param min_match_length: Minimum length of a match to be encoded as a reference
        """
        self.window_size = window_size
        self.min_match_length = min_match_length
    
    def compress(self, data):
        """
        Compress the input data using LZSS algorithm.
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as bytes
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return b''
        
        compressed = bytearray()
        current_pos = 0
        
        while current_pos < len(data):
            # Find the longest match in the sliding window
            best_match_length = 0
            best_match_offset = 0
            
            # Define the search range (sliding window)
            search_start = max(0, current_pos - self.window_size)
            search_end = current_pos
            
            for offset in range(search_start, search_end):
                match_length = 0
                
                # Check for match length
                while (current_pos + match_length < len(data) and 
                       match_length < 255 and  # Limit match length to 1 byte
                       data[offset + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if current match is longer
                if match_length > best_match_length and match_length >= self.min_match_length:
                    best_match_length = match_length
                    best_match_offset = current_pos - offset
            
            # Encode match or literal
            if best_match_length > 0:
                # Encode as a reference: (offset, length)
                # Use 2 bytes for offset, 1 byte for length
                compressed.append(0)  # Marker for match
                compressed.extend(best_match_offset.to_bytes(2, byteorder='big'))
                compressed.append(best_match_length)
                current_pos += best_match_length
            else:
                # Encode as a literal byte
                compressed.append(1)  # Marker for literal
                compressed.append(data[current_pos])
                current_pos += 1
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress data previously compressed with LZSS algorithm.
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data as bytes
        """
        # Validate input
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        current_pos = 0
        
        while current_pos < len(compressed_data):
            # Check marker byte
            marker = compressed_data[current_pos]
            current_pos += 1
            
            if marker == 0:  # Match
                # Read 2-byte offset and 1-byte length
                offset = int.from_bytes(compressed_data[current_pos:current_pos+2], byteorder='big')
                current_pos += 2
                match_length = compressed_data[current_pos]
                current_pos += 1
                
                # Reconstruct match from previous data
                start_pos = len(decompressed) - offset
                for i in range(match_length):
                    decompressed.append(decompressed[start_pos + i])
            
            elif marker == 1:  # Literal
                decompressed.append(compressed_data[current_pos])
                current_pos += 1
            
            else:
                raise ValueError(f"Invalid marker byte: {marker}")
        
        return bytes(decompressed)