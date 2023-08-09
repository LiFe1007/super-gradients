def import_onnx_graphsurgeon_or_fail_with_instructions():
    try:
        import onnx_graphsurgeon as gs
    except ImportError:
        raise ImportError(
            "onnx-graphsurgeon is required to use export API. "
            "Please install it with pip install onnx_graphsurgeon>=0.3.8,<0.4 --extra-index-url https://pypi.ngc.nvidia.com"
        )
    return gs
