def calculate_performance_metrics(transactions):
    read_latencies = []
    write_operations = 0
    total_bytes_transferred = 0
    timestamps = []

    for transaction in transactions:
        if transaction['TxnType'] == 'Rd' and 'Data' in transaction['Data']:
            latency = transaction['Timestamp'] - transactions[transaction['RefIndex']]['Timestamp']
            read_latencies.append(latency)
        if transaction['TxnType'] == 'Wr':
            write_operations += 1
            total_bytes_transferred += 32  # assuming fixed 32B per transfer
        timestamps.append(transaction['Timestamp'])

    average_latency = sum(read_latencies) / len(read_latencies) if read_latencies else 0
    total_time = max(timestamps) - min(timestamps) if timestamps else 0
    average_bandwidth = (total_bytes_transferred / total_time) if total_time else 0

    return average_latency, average_bandwidth

# Example transaction log
transactions = [
    {'Timestamp': 0, 'TxnType': 'Rd', 'Data': 'Data Addr1', 'RefIndex': 0},
    {'Timestamp': 2, 'TxnType': 'Wr', 'Data': 'Data Addr2'},
    {'Timestamp': 4, 'TxnType': 'Wr', 'Data': 'Data Addr3'},
    {'Timestamp': 10, 'TxnType': 'Rd', 'Data': 'Data Addr1', 'RefIndex': 0}
]

latency, bandwidth = calculate_performance_metrics(transactions)
print(f"Average Latency: {latency} cycles")
print(f"Average Bandwidth: {bandwidth} Bytes/sec")
