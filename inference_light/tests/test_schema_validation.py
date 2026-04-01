from __future__ import annotations

from pathlib import Path

from uninet_inference.io.schema_validation import (
    load_yaml_file,
    validate_compatibility_config,
    validate_datasets_config,
    validate_parameters_config,
    validate_prior_config,
    validate_run_config,
)


def test_default_configs_validate() -> None:
    project_root = Path(__file__).resolve().parents[1]
    config_dir = project_root / "configs"

    run_config = load_yaml_file(config_dir / "run.yaml")
    parameters_config = load_yaml_file(config_dir / "parameters.yaml")
    datasets_config = load_yaml_file(config_dir / "datasets.yaml")
    priors_regge_config = load_yaml_file(config_dir / "priors_regge.yaml")
    priors_efe_config = load_yaml_file(config_dir / "priors_efe.yaml")
    compatibility_config = load_yaml_file(config_dir / "compatibility.yaml")

    validate_run_config(run_config)
    validate_parameters_config(parameters_config)
    validate_datasets_config(datasets_config, project_root)
    known_parameters = set(parameters_config["parameters"].keys())
    validate_prior_config(priors_regge_config, known_parameters, "regge prior config")
    validate_prior_config(priors_efe_config, known_parameters, "efe prior config")
    validate_compatibility_config(compatibility_config)

