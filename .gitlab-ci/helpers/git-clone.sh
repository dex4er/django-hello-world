test -n "$GIT_REPO_URL" || exit 1

ARTIFACTS_REPO_NAME=${ARTIFACTS_REPO_NAME:-$(basename "$GIT_REPO_URL" .git)}
work_tree=".cache/repo/$ARTIFACTS_REPO_NAME"

git="${GIT:-git}"
git_work="env GIT_WORK_TREE=$work_tree GIT_DIR=$work_tree/.git git"

branch=${CI_COMMIT_REF_NAME:-$($git rev-parse --abbrev-ref HEAD)}

mkdir -p $(dirname $work_tree)

if [ ! -d $work_tree ]; then
    $git clone $GIT_REPO_URL $work_tree
else
    $git_work clean -dfx
    $git_work reset --hard
fi

$git_work checkout $branch || $git_work checkout -b $branch || exit 1
$git_work pull --ff-only origin $branch
