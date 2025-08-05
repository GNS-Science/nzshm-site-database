# Undoing a Release

If you create a release of the database in error follow these steps to roll back to the previous release.

On GitHub, go to releases

![releases](images/releases.png)

Click the delete icon for the release

![delete release](images/delete_release.png)

Click on tags and delete the tag

![tags](images/tags.png)
![delete tag](images/delete_tag.png)

Now you need to re-run the release process. Go to Actions

![actions](images/actions.png)

Click on "publish workflow"

![publish workflow](images/publish_workflow.png)

Click on "Run workflow" and select the most recent, correct tag.

![run workflow](images/run_workflow.png)