def stitch(ctx, source):

    nodes = source.get("services")

    if nodes:
        for n in nodes:
            deploy = n.get("deploy")
            if deploy is None:
                resources = {'resources':
                                {'limits':
                                    {'cpus': '0.25',
                                    'memory': '100M'},
                                'reservations':
                                    {'cpus': '0.25',
                                    'memory': '100M'}
                                }
                            }
                n.set("deploy", resources)

    return source
