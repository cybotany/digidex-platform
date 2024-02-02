from django.db import models

class Contact(models.Model):
    """
    Contact model for storing contact form submissions.

    Fields:
        name (CharField): The name of the person submitting the contact form.
        email (EmailField): The email address of the person submitting the form.
        message (TextField): The message content from the contact form.
        created_at (DateTimeField): The date and time when the contact form was submitted.
    """
    name = models.CharField(
        max_length=256,
        verbose_name="Name",
        help_text="The name of the person submitting the contact form."
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="The email address of the person submitting the contact form."
    )
    message = models.TextField(
        verbose_name="Message",
        help_text="The message content from the contact form."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the contact form was submitted."
    )

    def __str__(self):
        """
        Returns a string representation of a contact form submission.

        Returns:
            str: A string in the format "Contact submission from <name>".
        """
        return f"Contact submission from {self.name}"
