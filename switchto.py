import os
import re
import sys
import json
import socket
import argparse
import switchto_jmode

home_path = os.environ.get('HOME') or os.environ.get('HOMEPATH')
config_path = os.path.join(home_path, '.s2.json')

if not os.path.exists(config_path):
    config = {}
else:
    with open(config_path, 'r') as f:
        config = json.load(f)

def set_rules(domain, rules_dests, resolve):
    if domain not in config:
        config[domain] = {}

    for rule_dest in rules_dests:
        # TODO: check ':' exists
        if ':' not in rule_dest:
            print('expecting format rule:dest, got: "%s"' % rule_dest, file=sys.stderr)
            return

        rule, dest = rule_dest.split(':')
        # super simple IP regex
        # (empty destinations means delete entry)
        if dest and not re.match('^[\d\.:]+$', dest):
            if resolve:
                original_host = dest
                dest = socket.gethostbyname(original_host)
                print('resolved "%s" to %s' % (original_host, dest))
            else:
                # this is because I'm using hosts file, not a DNS which would allow CNAMEs
                # maybe next time... ;)
                print('cannot set domain to resolve to another domain. pass -y to resolve "%s" now' % dest, file=sys.stderr)
                return

        config[domain][rule] = dest

    save_config()

def save_config():
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

def list_rules(filters):
    if not filters:
        return config

    # so I can use ^$ in multiline regex
    filters = '\n'.join(filters)
    output = {}
    for domain, rules in config.items():
        for rule in rules:
            if re.match('^%s$' % domain, filters) or re.match('^%s$' % rule, filters, re.MULTILINE):
                if domain not in output:
                    output[domain] = {}

                output[domain][rule] = config[domain][rule]

    return output

def print_rules(rules):
    print(json.dumps(rules, indent=2))

def run_hostsman(*args):
    import hostsman

    sys.argv = ['hostsman'] + list(args)
    print(sys.argv)
    hostsman.main()

def switchto(rule):
    remove_domains = []
    insert_rules = []
    for domain, rules in config.items():
        # TODO: consider adding "-f" so if and only if specified, when rule is
        # undefined (as opposed to empty string) it will remove the entry from hosts
        if rule not in rules or not config[domain][rule]:
            remove_domains.append(domain)
        else:
            dest = config[domain][rule]
            hostsman_rule = '%s:%s' % (domain, dest)
            insert_rules.append(hostsman_rule)

    if remove_domains:
        run_hostsman('-r', *remove_domains)
    
    if insert_rules:
        run_hostsman('-i', *insert_rules)

def main():
    parser = argparse.ArgumentParser(description='redirect domains to dev servers and back to production')
    parser.add_argument('-l', '-list', dest='list', nargs='*',
                        help='list [rule|domain [...]]')
    # TODO: verbosity is always a good idea
    #parser.add_argument('-v', '-verbose', dest='verbose', action='store_true',
    #                    help='verbose')
    parser.add_argument('-j', '-J', dest='j', action='store_true',
                        help='enables J-mode')
    parser.add_argument('-s', '-set', dest='set', nargs='+',
                        help='set domain rule:dest [rule:dest [...]]')
    parser.add_argument('-y', '-yes', dest='yes', action='store_true',
                        help='whether or not to convert target hosts to IP')
    parser.add_argument('to', nargs='?',
                        help='rule')

    args = parser.parse_args()

    if args.set:
        set_rules(args.set[0], args.set[1:], args.yes)

    if args.list is not None:
        rules = list_rules(args.list)
        print_rules(rules)

    if args.to:
        switchto(args.to)

    if args.j:
        switchto_jmode.jmode()

if __name__ == '__main__':
    main()
