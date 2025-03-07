from dbt.artifacts.resources.base import BaseResource, GraphResource

# alias to latest resource definitions
from dbt.artifacts.resources.v1.components import DependsOn, NodeVersion, RefArgs
from dbt.artifacts.resources.v1.documentation import Documentation
from dbt.artifacts.resources.v1.exposure import (
    Exposure,
    ExposureConfig,
    ExposureType,
    MaturityType,
)
from dbt.artifacts.resources.v1.macro import Macro, MacroDependsOn, MacroArgument
from dbt.artifacts.resources.v1.docs import Docs
from dbt.artifacts.resources.v1.group import Group
from dbt.artifacts.resources.v1.metric import (
    ConstantPropertyInput,
    ConversionTypeParams,
    Metric,
    MetricConfig,
    MetricInput,
    MetricInputMeasure,
    MetricTimeWindow,
    MetricTypeParams,
)
from dbt.artifacts.resources.v1.owner import Owner
from dbt.artifacts.resources.v1.saved_query import (
    Export,
    ExportConfig,
    QueryParams,
    SavedQuery,
    SavedQueryConfig,
    SavedQueryMandatory,
)
from dbt.artifacts.resources.v1.semantic_layer_components import (
    FileSlice,
    SourceFileMetadata,
    WhereFilter,
    WhereFilterIntersection,
)
from dbt.artifacts.resources.v1.semantic_model import (
    Defaults,
    Dimension,
    DimensionTypeParams,
    DimensionValidityParams,
    Entity,
    Measure,
    MeasureAggregationParameters,
    NodeRelation,
    NonAdditiveDimension,
    SemanticModel,
    SemanticModelConfig,
)
