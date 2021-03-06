workflow "example" {
    resolves = ["b"]
}

action "a" {
    uses = "$_VAR1"
    args = "$_VAR2"
}

action "b" {
    needs = "a"
    uses = "$_VAR1"
    args = "$_VAR2"
    runs = "$_VAR4"
    secrets = ["$_VAR5"]
    env = {
        "$_VAR6" = "$_VAR7"
    }
}
