#!/usr/bin/env python3
"""Executive Cyber-Risk & Risk Advocacy Suite.

A standard-library-only, educational GRC decision-support CLI. Its generated
mappings and recommendations are starting points for qualified human review;
they do not certify compliance or replace legal, security, or audit advice.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Sequence, Tuple


class InputValidationError(ValueError):
    """Raised when a value is outside the application's supported range."""


def _choice(prompt: str, choices: Sequence[str]) -> str:
    """Prompt until the user enters a listed, case-insensitive choice."""
    normalized = {value.lower(): value for value in choices}
    numbered = {str(index): value for index, value in enumerate(choices, start=1)}
    while True:
        answer = input(prompt).strip().lower()
        if answer in normalized:
            return normalized[answer]
        if answer in numbered:
            return numbered[answer]
        print("Please choose one of: " + ", ".join(choices))


def _text(prompt: str, *, allow_empty: bool = False) -> str:
    while True:
        answer = input(prompt).strip()
        if answer or allow_empty:
            return answer
        print("A value is required.")


def _number(prompt: str, *, minimum: float, maximum: float,
            allow_zero: bool = True) -> float:
    while True:
        raw = input(prompt).strip().replace(",", "")
        try:
            value = float(raw)
        except ValueError:
            print("Enter a number, such as 25000 or 0.25.")
            continue
        if value != value or value in (float("inf"), float("-inf")):
            print("Enter a finite number.")
            continue
        if (value < minimum or value > maximum or
                (not allow_zero and value == 0)):
            qualifier = "greater than zero" if not allow_zero else f"between {minimum:g} and {maximum:g}"
            print(f"Enter a value {qualifier}.")
            continue
        return value


def _integer(prompt: str, *, minimum: int, maximum: int) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Enter a whole number.")
            continue
        if not minimum <= value <= maximum:
            print(f"Enter a whole number from {minimum} to {maximum}.")
            continue
        return value


def _money(value: float) -> str:
    return f"${value:,.2f}"


def _bar(title: str) -> None:
    width = max(62, len(title) + 4)
    print("+" + "-" * (width - 2) + "+")
    print("| " + title.center(width - 4) + " |")
    print("+" + "-" * (width - 2) + "+")


# Project 1: mappings are intentionally framed as control considerations,
# not claims that selecting a deployment topology proves framework compliance.
@dataclass(frozen=True)
class AIProfile:
    deployment: str
    sensitivity: str
    safeguards: Tuple[str, ...]
    risk_warnings: Tuple[str, ...]
    nist_functions: Tuple[str, ...]
    iso_topics: Tuple[str, ...]


class AIPolicySimulator:
    """Map deployment and information sensitivity to governance safeguards."""

    DEPLOYMENTS = ("Public Cloud Endpoint", "Isolated Cloud VPC", "Local OS Model Deployment")
    SENSITIVITY = ("Public", "Internal", "Confidential", "Restricted")

    def assess(self, deployment: str, sensitivity: str,
               handles_personal_data: bool = False,
               enables_external_actions: bool = False) -> AIProfile:
        deployment = self._validate(deployment, self.DEPLOYMENTS, "deployment")
        sensitivity = self._validate(sensitivity, self.SENSITIVITY, "sensitivity")
        safeguards: List[str] = [
            "Assign an accountable AI system owner and record intended use, users, and prohibited uses.",
            "Inventory the model, provider, version, connected tools, data flows, and business process.",
            "Document human oversight, incident escalation, change approval, and periodic review.",
            "Test for prompt injection, insecure output handling, data leakage, and unsafe tool use before release.",
            "Maintain evidence for risk decisions and map applicable controls to the organization's chosen framework scope.",
        ]
        warnings: List[str] = []
        if deployment == "Public Cloud Endpoint":
            safeguards += [
                "Review provider retention, training-use, subprocessors, breach notice, and deletion terms before sending data.",
                "Use approved tenant controls, strong authentication, least privilege, and egress monitoring.",
            ]
            warnings.append("A public endpoint can expose prompts or outputs to provider-side processing; verify contractual and technical data protections.")
        elif deployment == "Isolated Cloud VPC":
            safeguards += [
                "Validate network isolation, private routing, key ownership, identity boundaries, and administrative access logging.",
                "Confirm model hosting and support paths do not bypass the intended tenant boundary.",
            ]
            warnings.append("A private network boundary does not by itself prevent data misuse, compromised credentials, or unsafe model outputs.")
        else:
            safeguards += [
                "Harden the host, restrict model and package provenance, patch dependencies, and control local administrator access.",
                "Define local storage, backup, removable-media, and model-update controls.",
            ]
            warnings.append("Local hosting shifts more patching, physical security, monitoring, and model integrity responsibility to the organization.")
        sensitivity_index = self.SENSITIVITY.index(sensitivity)
        if sensitivity_index >= 2:
            safeguards += [
                "Minimize or redact sensitive inputs; prohibit unapproved production secrets and credentials in prompts.",
                "Require documented privacy/security approval, retention limits, access review, and a tested deletion path.",
            ]
        if sensitivity == "Restricted":
            warnings.append("Restricted data requires explicit owner approval and verified safeguards; do not rely on this simulator as authorization to process it.")
        if handles_personal_data:
            safeguards.append("Complete a privacy impact review and confirm the lawful purpose, notices, retention, and individual-rights workflow.")
        if enables_external_actions:
            safeguards += [
                "Require human approval for consequential external actions and enforce allowlists, scoped credentials, and transaction limits.",
                "Log tool calls and test prompt injection paths that could influence connected systems.",
            ]
            warnings.append("Connected actions increase the impact of prompt injection and compromised or misleading model output.")
        return AIProfile(
            deployment, sensitivity, tuple(safeguards), tuple(warnings),
            ("Govern", "Map", "Measure", "Manage"),
            ("AI management system scope and policy", "Risk assessment and treatment", "Operational controls and monitoring", "Documented information and continual improvement"),
        )

    @staticmethod
    def _validate(value: str, allowed: Sequence[str], label: str) -> str:
        for option in allowed:
            if value.strip().lower() == option.lower():
                return option
        raise InputValidationError(f"Unsupported {label}. Choose one of: {', '.join(allowed)}")


# Project 2: ALE follows the blueprint's SLE * ARO equation. ROI is an
# estimate based on user-entered residual-risk reduction and annual control cost.
@dataclass(frozen=True)
class RiskAssessment:
    asset_name: str
    asset_value: float
    exposure_factor: float
    annualized_rate: float
    sle: float
    ale: float
    cc6_1_status: str
    cc6_1_gaps: Tuple[str, ...]
    cc7_5_status: str
    cc7_5_gaps: Tuple[str, ...]
    expected_annual_savings: float
    annual_control_cost: float
    net_annual_benefit: float
    roi_percent: Optional[float]
    payback_years: Optional[float]


class GRCRiskEngine:
    """Calculate SLE/ALE and estimate controls' financial value."""

    CONTROL_STATUSES = ("Implemented", "Partially implemented", "Not implemented", "Not assessed")

    def assess(self, *, asset_name: str, asset_value: float,
               exposure_factor: float, annualized_rate: float,
               risk_reduction: float, annual_control_cost: float,
               cc6_1_status: str, cc6_1_gaps: Sequence[str],
               cc7_5_status: str, cc7_5_gaps: Sequence[str]) -> RiskAssessment:
        if not asset_name.strip():
            raise InputValidationError("Asset name cannot be empty.")
        self._range("asset value", asset_value, 0.01, 1e15)
        self._range("exposure factor", exposure_factor, 0.0, 1.0)
        self._range("annualized rate of occurrence", annualized_rate, 0.0, 100.0)
        self._range("risk reduction", risk_reduction, 0.0, 1.0)
        self._range("annual control cost", annual_control_cost, 0.0, 1e15)
        if cc6_1_status not in self.CONTROL_STATUSES or cc7_5_status not in self.CONTROL_STATUSES:
            raise InputValidationError("SOC 2 control statuses must be Implemented, Partially implemented, Not implemented, or Not assessed.")
        sle = asset_value * exposure_factor
        ale = sle * annualized_rate
        savings = ale * risk_reduction
        net = savings - annual_control_cost
        roi = ((net / annual_control_cost) * 100.0
               if annual_control_cost > 0 else None)
        payback = (annual_control_cost / savings
                   if savings > 0 else None)
        return RiskAssessment(
            asset_name.strip(), asset_value, exposure_factor, annualized_rate,
            sle, ale, cc6_1_status, tuple(cc6_1_gaps), cc7_5_status,
            tuple(cc7_5_gaps), savings,
            annual_control_cost, net, roi, payback,
        )

    @staticmethod
    def _range(label: str, value: float, minimum: float, maximum: float) -> None:
        if value != value or value in (float("inf"), float("-inf")) or not minimum <= value <= maximum:
            raise InputValidationError(f"{label} must be between {minimum:g} and {maximum:g}.")


# Project 3: scoring is fully visible and adjustable at source. A score of 5
# means strongest evidence/control maturity for that dimension.
@dataclass(frozen=True)
class VendorAssessment:
    vendor_name: str
    dimension_scores: Dict[str, int]
    total_score: float
    decision: str
    directives: Tuple[str, ...]
    evidence_gaps: Tuple[str, ...]


class VendorRFPMatrix:
    """Score five vendor security dimensions and produce SOW guidance."""

    WEIGHTS: Dict[str, int] = {
        "Data transit protection": 25,
        "IAM boundaries": 25,
        "External certifications": 20,
        "Log isolation and access": 15,
        "Data residency and deletion": 15,
    }

    def assess(self, vendor_name: str, scores: Dict[str, int],
               *, pass_threshold: float = 80.0,
               conditional_threshold: float = 60.0) -> VendorAssessment:
        if not vendor_name.strip():
            raise InputValidationError("Vendor name cannot be empty.")
        if set(scores) != set(self.WEIGHTS):
            missing = sorted(set(self.WEIGHTS) - set(scores))
            extra = sorted(set(scores) - set(self.WEIGHTS))
            raise InputValidationError(f"Provide exactly the five scoring dimensions. Missing: {missing}; unexpected: {extra}.")
        for dimension, score in scores.items():
            if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 5:
                raise InputValidationError(f"{dimension} score must be a whole number from 0 to 5.")
        if not 0 <= conditional_threshold < pass_threshold <= 100:
            raise InputValidationError("Thresholds must satisfy 0 <= conditional < pass <= 100.")
        total = sum(scores[name] / 5 * weight for name, weight in self.WEIGHTS.items())
        decision = "PASS" if total >= pass_threshold else "CONDITIONAL" if total >= conditional_threshold else "FAIL"
        directives: List[str] = []
        contract_by_dimension = {
            "Data transit protection": "Require encryption in transit, approved protocols, key management responsibilities, and breach notification timelines.",
            "IAM boundaries": "Require SSO/MFA where applicable, named roles, least privilege, prompt offboarding, and periodic access evidence.",
            "External certifications": "Define required independent assurance evidence, scope, report dates, exceptions, and remediation updates.",
            "Log isolation and access": "Define log ownership, tenant separation, access restrictions, retention, export, and incident access procedures.",
            "Data residency and deletion": "Specify approved processing/storage regions, subprocessors, return/deletion timing, and deletion attestation.",
        }
        gaps = tuple(name for name, score in scores.items() if score <= 2)
        if decision == "FAIL":
            directives.append("Do not onboard until material security gaps are remediated and independently evidenced.")
        elif decision == "CONDITIONAL":
            directives.append("Use only after risk-owner approval, a time-bound remediation plan, and compensating controls are documented.")
        else:
            directives.append("Proceed subject to normal due diligence, contract review, and ongoing monitoring.")
        for name in gaps:
            directives.append(contract_by_dimension[name])
        if not gaps:
            directives.append("Attach the reviewed evidence set, scope assumptions, and reassessment date to the procurement record.")
        return VendorAssessment(vendor_name.strip(), dict(scores), total, decision,
                                tuple(directives), gaps)


def _run_ai(simulator: AIPolicySimulator) -> None:
    _bar("PROJECT 1 | AI POLICY SIMULATOR")
    print("Choose the deployment and highest data sensitivity involved.")
    deployment = _choice("Deployment [1] Public Cloud Endpoint [2] Isolated Cloud VPC [3] Local OS Model Deployment: ",
                         simulator.DEPLOYMENTS)
    sensitivity = _choice("Sensitivity [1] Public [2] Internal [3] Confidential [4] Restricted: ",
                          simulator.SENSITIVITY)
    personal = _choice("Does it process personal data? [y/n]: ", ("y", "n")) == "y"
    actions = _choice("Can it take external actions or call tools? [y/n]: ", ("y", "n")) == "y"
    result = simulator.assess(deployment, sensitivity, personal, actions)
    print(f"\nProfile: {result.deployment} | {result.sensitivity} data")
    print("NIST AI RMF functions to consider: " + ", ".join(result.nist_functions))
    print("ISO/IEC 42001 topics to consider: " + "; ".join(result.iso_topics))
    for warning in result.risk_warnings:
        print("WARNING: " + warning)
    print("Safeguards to validate:")
    for item in result.safeguards:
        print(f"  - {item}")


def _run_grc(engine: GRCRiskEngine) -> None:
    _bar("PROJECT 2 | QUANTITATIVE GRC RISK ENGINE")
    asset = _text("Asset / business process name: ")
    value = _number("Asset value in currency units: ", minimum=0.01, maximum=1e15, allow_zero=False)
    exposure = _number("Exposure factor (0.0 to 1.0): ", minimum=0.0, maximum=1.0)
    aro = _number("Annualized rate of occurrence (events/year; e.g. 0.2): ", minimum=0.0, maximum=100.0)
    reduction = _number("Estimated risk reduction from proposed control (0.0 to 1.0): ", minimum=0.0, maximum=1.0)
    cost = _number("Annual control cost: ", minimum=0.0, maximum=1e15)
    statuses = engine.CONTROL_STATUSES
    cc6_status = _choice("CC6.1 logical access control status [1] Implemented [2] Partially implemented [3] Not implemented [4] Not assessed: ", statuses)
    cc75_status = _choice("CC7.5 security-incident recovery status [1] Implemented [2] Partially implemented [3] Not implemented [4] Not assessed: ", statuses)
    print("Enter related evidence gaps separated by commas. Leave blank when none are identified.")
    cc6 = [x.strip() for x in input("CC6.1 logical access evidence gaps: ").split(",") if x.strip()]
    cc75 = [x.strip() for x in input("CC7.5 incident recovery / testing evidence gaps: ").split(",") if x.strip()]
    result = engine.assess(asset_name=asset, asset_value=value,
                           exposure_factor=exposure, annualized_rate=aro,
                           risk_reduction=reduction, annual_control_cost=cost,
                           cc6_1_status=cc6_status, cc6_1_gaps=cc6,
                           cc7_5_status=cc75_status, cc7_5_gaps=cc75)
    print("\nFormula: SLE = asset value x exposure factor; ALE = SLE x annualized rate.")
    print(f"SLE: {_money(result.sle)}")
    print(f"ALE: {_money(result.ale)} per year")
    print(f"Estimated annual loss reduction: {_money(result.expected_annual_savings)}")
    print(f"Annual control cost: {_money(result.annual_control_cost)}")
    print(f"Estimated net annual benefit: {_money(result.net_annual_benefit)}")
    print("Estimated ROI: " + (f"{result.roi_percent:.1f}%" if result.roi_percent is not None else "not calculated (control cost is zero)"))
    print("Estimated payback: " + (f"{result.payback_years:.2f} years" if result.payback_years is not None else "not calculated (no estimated loss reduction)"))
    print(f"CC6.1 logical access status: {result.cc6_1_status}")
    print("  Evidence gaps: " + ("; ".join(result.cc6_1_gaps) if result.cc6_1_gaps else "none entered"))
    print(f"CC7.5 incident recovery status: {result.cc7_5_status}")
    print("  Evidence gaps: " + ("; ".join(result.cc7_5_gaps) if result.cc7_5_gaps else "none entered"))
    print("Financial outputs are scenario estimates; validate asset values, occurrence rates, and control effects with owners.")


def _run_vendor(matrix: VendorRFPMatrix) -> None:
    _bar("PROJECT 3 | VENDOR RFP & SOW RISK MATRIX")
    vendor = _text("Vendor / product name: ")
    scores: Dict[str, int] = {}
    for name in matrix.WEIGHTS:
        print(f"{name} (0 = absent/poor evidence, 5 = strong verified evidence)")
        scores[name] = _integer("  Score [0-5]: ", minimum=0, maximum=5)
    result = matrix.assess(vendor, scores)
    print(f"\nWeighted score: {result.total_score:.1f}/100")
    print(f"Decision: {result.decision}")
    print("Dimension breakdown:")
    for name, weight in matrix.WEIGHTS.items():
        print(f"  {name}: {scores[name]}/5 (weight {weight}%)")
    print("SOW / procurement directives:")
    for directive in result.directives:
        print(f"  - {directive}")
    if result.evidence_gaps:
        print("Low-scoring evidence areas: " + ", ".join(result.evidence_gaps))
    print("Use this matrix as procurement guidance; legal counsel and the risk owner should review final contract language.")


def main() -> int:
    """Run the interactive application; return a process exit code."""
    _bar("EXECUTIVE CYBER-RISK & RISK ADVOCACY SUITE")
    print("Three practical decision-support tools for GRC and consulting portfolios.")
    print("Advisory only: outputs are not a compliance attestation or legal opinion.\n")
    actions: Dict[str, Callable[[], None]] = {
        "1": lambda: _run_ai(AIPolicySimulator()),
        "2": lambda: _run_grc(GRCRiskEngine()),
        "3": lambda: _run_vendor(VendorRFPMatrix()),
    }
    while True:
        print("\n[1] AI governance policy simulator")
        print("[2] Quantitative GRC risk register")
        print("[3] Vendor RFP / SOW risk matrix")
        print("[q] Quit")
        selected = _choice("Select a project: ", ("1", "2", "3", "q"))
        if selected == "q":
            print("Goodbye.")
            return 0
        try:
            actions[selected]()
        except (InputValidationError, EOFError, KeyboardInterrupt) as exc:
            if isinstance(exc, (EOFError, KeyboardInterrupt)):
                print("\nInput cancelled. Returning to the main menu.")
            else:
                print(f"\nInput error: {exc}")
        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    raise SystemExit(main())
