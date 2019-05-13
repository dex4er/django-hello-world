test -n "$ARTIFACTS_PATH" || exit 1
test -d "$ARTIFACTS_PATH" || exit 1

. .gitlab-ci/helpers/git-clone.sh

rm -rf $work_tree/*
cp -a $ARTIFACTS_PATH/* $work_tree

$git_work add .

if $git_work diff --cached --stat --exit-code; then
    empty=" (no changes)"
else
    empty=""
fi

$git_work commit . --allow-empty --message="New pipeline #$CI_PIPELINE_ID for $CI_COMMIT_SHORT_SHA$empty"
$git_work push -o ci.skip origin $brach
