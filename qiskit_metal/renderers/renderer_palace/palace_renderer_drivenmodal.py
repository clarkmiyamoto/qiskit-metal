from qiskit_metal.renderers.renderer_palace.palace_renderer_base import QPalaceRenderer

class QDrivenmodalPalace(QPalaceRenderer):
    
    name = "palace_drivenmodal"
    """Name"""

    default_setup = Dict(
        name="QHFSSDrivenmodalPyaedt_setup",
        Frequency="5.0",  # GHz
        MaxDeltaE="0.01",
        MaximumPasses="10",
        MinimumPasses="1",
        MinimumConvergedPasses="1",
        PercentRefinement="30",
        BasisOrder="1",
    )
    """Palace Drivenmodal Options"""

    def __init__(self,
                 design: 'MultiPlanar',
                 layer_types: Union[dict, None] = None,
                 initiate: bool = True,
                 options: Dict = None):

        super().__init__(design=design, initiate=initiate, options=options)

    def run(self):
        pass