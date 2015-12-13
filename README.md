# parse_iwlist
Quick script to parse iwlist scan output into a bar chart.

```bash
watch "sudo iwlist <wifi_interface> scan | python3 parse.py"
```

Note: root is required to trigger a new scan each time.

