import dns.resolver
import json


def test_lookup(request):
    svc = request.args.get('svc')
    if svc:
        return lookup(svc)
    return 'svc arg not provided'


def lookup(name):
    answers = dns.resolver.query(f'_run._tcp.{name}.svc.local.', 'SRV')
    if answers:
        print(f'found answers {answers} for name: {name}')
        return f'host: {answers[0].target} port: {answers[0].port}'
    else:
        print(f'no answers found for {name}')
        return None
