try:
    from cdci_data_analysis.analysis.exceptions import RequestNotUnderstood
    # special treatment of this exception when working with dispatcher 
except ImportError:
    class RequestNotUnderstood(RuntimeError): pass