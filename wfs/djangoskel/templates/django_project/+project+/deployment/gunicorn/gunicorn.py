import multiprocessing


bind = '127.0.0.1:8000'
workers = multiprocessing.cpu_count() * 2 + 1

def post_fork(server, worker):
    import monitor
    import settings
    if settings.DEBUG:
        server.log.info("Starting change monitor.")
        monitor.start(interval=1.0)
