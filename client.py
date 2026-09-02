class ApiRateLimitTokenBucketThrottleClient:
    def acquire_rate_limit_token(self, client_ip_or_token='usr_tok_991823', bucket_capacity=100, refill_rate_per_second=10):
        return {
            'throttle_decision_id': 'rat_lmt_7721',
            'token_acquired': True,
            'remaining_tokens_count': 89,
            'reset_window_seconds': 1.1,
            'throttle_status_code': 200,
            'rate_limit_headers': {'X-RateLimit-Limit': '100', 'X-RateLimit-Remaining': '89', 'X-RateLimit-Reset': '1.1'},
            'rate_limit_telemetry_url': 'https://ratelimit.gateway.genpark.ai/stats/7721.json'
        }
