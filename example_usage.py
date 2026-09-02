from client import ApiRateLimitTokenBucketThrottleClient

def main():
    client = ApiRateLimitTokenBucketThrottleClient()
    res = client.acquire_rate_limit_token('ip_192_168_1_1', 60, 5)
    print('Rate Limit Token Bucket: ' + res['throttle_decision_id'] + ' (Allowed: ' + str(res['token_acquired']) + ')')
    print('Remaining Tokens: ' + str(res['remaining_tokens_count']) + ' | Reset in: ' + str(res['reset_window_seconds']) + 's')
    print('Telemetry URL: ' + res['rate_limit_telemetry_url'])

if __name__ == '__main__':
    main()
