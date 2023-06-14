class QEigenmodePalace(QPalaceRenderer):

    name = "palace_eigenmode"
    """Name"""
    
    default_setup = Dict(
        name="QHFSSEigenmodePyaedt_setup",
        MinimumFrequency="5.0",  # GHz
        NumModes="1",
        MaxDeltaFreq="0.5",
        MaximumPasses="10",
        MinimumPasses="1",
        MinimumConvergedPasses="1",
        PercentRefinement="30",
        BasisOrder="1")
    """Palace Eigenmode Options"""
    
    def __init__(self,
                 design: 'MultiPlanar',
                 layer_types: Union[dict, None] = None,
                 initiate: bool = True,
                 options: Dict = None):

        super().__init__(design=design, initiate=initiate, options=options)

