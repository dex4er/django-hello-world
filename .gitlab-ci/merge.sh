test -n "$GIT_MERGE_FROM" || exit 1

. .gitlab-ci/helpers/git-clone.sh

$git_work checkout $branch || $git_work checkout -b $branch || exit 1
$git_work merge ${GIT_MERGE_MODE:---ff-only} $GIT_MERGE_FROM

$git_work push origin $branch
