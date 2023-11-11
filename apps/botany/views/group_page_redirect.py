def get_success_url(self, group_position):
    """
    Returns the URL to redirect to after successfully updating a plant.
    """
    if group_position is not None:
        return reverse('your_view_name') + f"?page={group_position}"
    else:
        return reverse('botany:home')