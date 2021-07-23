import dns.resolver


def test_lookup(request):
    args = request.args
    result = ''
    if args and 'svc' in args:
        result = lookup(args['svc'])


def lookup(name):
    answers = dns.resolver.query(f'_run._tcp.{name}.svc.local.', 'SRV')
    if answers:
        return answers[0]
    else:
        return None
