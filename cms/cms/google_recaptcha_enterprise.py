from django.conf import settings
from google.cloud import recaptchaenterprise_v1
import logging

logger = logging.getLogger(__name__)

def validate_recaptcha(token: str, recaptcha_action: str) -> dict:
    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()
    project_name = f"projects/{settings.GOOGLE_CLOUD_PROJECT_ID}"

    try:
        response = client.create_assessment(
            recaptchaenterprise_v1.CreateAssessmentRequest(
                parent=project_name,
                assessment=recaptchaenterprise_v1.Assessment(
                    event=recaptchaenterprise_v1.Event(
                        site_key=settings.RECAPTCHA_SITE_KEY,
                        token=token
                    )
                )
            )
        )
    except Exception as e:
        logger.error(f"Failed to create reCAPTCHA assessment: {e}")
        return {"success": False, "message": str(e)}

    if not response.token_properties.valid:
        reason = response.token_properties.invalid_reason
        logger.warning(f"Invalid reCAPTCHA token: {reason}")
        return {"success": False, "message": f"Invalid token: {reason}"}

    if response.token_properties.action != recaptcha_action:
        logger.warning("Mismatched reCAPTCHA action.")
        return {"success": False, "message": "Mismatched action"}

    if response.risk_analysis.score < settings.RECAPTCHA_REQUIRED_SCORE:
        logger.info(f"reCAPTCHA score too low: {response.risk_analysis.score}")
        return {"success": False, "message": "Score too low"}

    return {"success": True, "message": "Validation successful", "score": response.risk_analysis.score}
