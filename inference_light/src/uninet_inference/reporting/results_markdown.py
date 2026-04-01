from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _format_interval(low: float, high: float) -> str:
    return f"[{low:.6g}, {high:.6g}]"


def build_results_markdown(
    run_id: str,
    seed: int,
    sampler_config: dict[str, Any],
    dataset_manifest: dict[str, Any],
    prior_snapshot: dict[str, Any],
    posterior_rows: list[dict[str, Any]],
    compatibility: dict[str, Any],
) -> str:
    timestamp = datetime.now(timezone.utc).isoformat()
    lines: list[str] = []
    lines.append("# InferenceLight Results")
    lines.append("")
    lines.append("## 1. Run Metadata")
    lines.append("")
    lines.append(f"- run_id: `{run_id}`")
    lines.append(f"- timestamp_utc: `{timestamp}`")
    lines.append(f"- seed: `{seed}`")
    lines.append(f"- sampler: `{sampler_config}`")
    lines.append("")
    lines.append("## 2. Dataset Manifest")
    lines.append("")
    lines.append("| dataset_id | family | version | source_url |")
    lines.append("|---|---|---|---|")
    for item in dataset_manifest["datasets"]:
        lines.append(
            f"| {item['dataset_id']} | {item['family']} | {item['version_tag']} | {item['source_url']} |"
        )
    lines.append("")
    lines.append("## 3. Prior Summary")
    lines.append("")
    lines.append(f"- regge_prior_count: `{len(prior_snapshot['regge'])}`")
    lines.append(f"- efe_prior_count: `{len(prior_snapshot['efe'])}`")
    lines.append("")
    lines.append("## 4. Parameter Ranges")
    lines.append("")
    lines.append("| parameter | median | 68% interval | 95% interval |")
    lines.append("|---|---:|---|---|")
    for row in posterior_rows:
        lines.append(
            "| {parameter} | {median:.6g} | {i68} | {i95} |".format(
                parameter=row["parameter"],
                median=row["median"],
                i68=_format_interval(row["p16"], row["p84"]),
                i95=_format_interval(row["p2p5"], row["p97p5"]),
            )
        )
    lines.append("")
    lines.append("## 5. Per-Dataset Compatibility")
    lines.append("")
    lines.append("| dataset_id | chi2_median | dof | sigma_equivalent | p_value | class |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for row in compatibility["datasets"]:
        lines.append(
            "| {dataset_id} | {chi2:.6g} | {dof} | {sigma:.6g} | {p:.6g} | {clazz} |".format(
                dataset_id=row["dataset_id"],
                chi2=row["chi2_median"],
                dof=row["dof"],
                sigma=row["sigma_equivalent"],
                p=row["posterior_predictive_p_value"],
                clazz=row["compatibility_class"],
            )
        )
    lines.append("")
    lines.append("## 6. Overall Verdict")
    lines.append("")
    lines.append(f"- traffic_light: `{compatibility['traffic_light']}`")
    lines.append(
        "- fits_known_physics_at_all: "
        f"`{str(compatibility['fits_known_physics_at_all']).lower()}`"
    )
    lines.append("")
    lines.append(
        "Interpretation: this is a compatibility-first verdict based on compressed "
        "datasets and model priors, not a final precision cosmology result."
    )
    lines.append("")
    return "\n".join(lines)

