from braincode_loop.decision import build_history_record, decide
from braincode_loop.doc_hygiene import HygieneResult

OK = HygieneResult(ok=True)
BAD = HygieneResult(ok=False, failures=[{"construct_name": "x", "missing_fields": ["glossary_gloss"]}])


def test_hygiene_failure_overrides_accept():
    assert decide(BAD, {"decision": "accept"}) == "needs-rework"


def test_critic_decisions_map():
    assert decide(OK, {"decision": "accept"}) == "accepted"
    assert decide(OK, {"decision": "Accepted"}) == "accepted"
    assert decide(OK, {"decision": "needs-rework"}) == "needs-rework"
    assert decide(OK, {"decision": "reject"}) == "rejected"


def test_unknown_decision_is_rework():
    assert decide(OK, {}) == "needs-rework"
    assert decide(OK, {"decision": "maybe"}) == "needs-rework"


def test_history_record_shape():
    proposal = {"changes": [{"op": "add", "construct_name": "a", "change_type": "MINOR"}]}
    critique = {"kpi_assessment": {"coverage": {"impact": "benefit"}}, "simulations": [{"item_id": "i"}], "cross_check": {"used": False}}
    rec = build_history_record(sprint=3, attempt=2, proposal=proposal, hygiene=OK, critique=critique, decision="accepted", cross_check_note="skipped")
    assert rec["sprint"] == 3 and rec["attempt"] == 2
    assert rec["changes"] == [{"op": "add", "construct_name": "a", "change_type": "MINOR"}]
    assert rec["simulations"] == [{"item_id": "i"}]
    assert rec["cross_check"] == {"used": False, "script_note": "skipped"}
