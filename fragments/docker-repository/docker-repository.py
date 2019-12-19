def stitch(ctx, source):

    nodes = source.get("services")

    if nodes:
        for n in nodes:
            image = n.get("image")
            if image:
                s = image.textValue()
                n.put("image", "registry-1.docker.io/%s" % s)

    return source
