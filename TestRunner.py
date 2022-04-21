import sys
import json
#from behave import __main__ as pythnoic_runner
import shutil
#import glob
import allure
import os
import pickle
from behave import __main__ as testrunner
from dotenv import load_dotenv
import datetime

browserstack_device = ''
global device_os_version
browserstack_build = ""
userName = ""
accessKey = ""
browserstack_appUrl = ""

data = json.load(open("Features/Resources/config.json"))
HOME_DIR = os.getcwd()
data["HOME_DIR"] = HOME_DIR
print("Home - "+HOME_DIR)
load_dotenv(verbose=True, dotenv_path=os.path.join(data["HOME_DIR"], ".env"))


def get_tags():
    # --tags @dev,@wip,~@bar
    # --tags=dev,wip
    tags_to_include = os.getenv("TAG", "all")
    print(tags_to_include)
    tags_to_exclude = os.getenv("EXCLUDE", None)
    print(tags_to_exclude)

    tag_include_list = tags_to_include.split(",")
    cmd = "--tags=" + ",".join(tag_include_list)
    print(cmd)

    if tags_to_exclude:
        tag_exclude_list = tags_to_exclude.split(",")
        cmd = cmd + ",~" + ",~".join(tag_exclude_list)
    return cmd

def main():
    """
    Pythonic Runner
    """
    sys.stdout.flush()
    # rerun_failures_flag = bool(os.getenv("RERUN_ONLY_FAILURES", False))
    # if rerun_failures_flag:
    #     args = "rerun.txt"
    #
    # else:
    log_args = "--no-capture --format rerun --outfile "
    tag_args = get_tags()
    skipped_args = "--no-skipped"     # --show-skipped/--no-skipped
    report_args = "-f allure"
    output_args = "-o reports-json"
    features_args = "Features/."
    browserstack_device = os.getenv("BROWSERSTACK_DEVICE")
    device_os_version = os.getenv("OS_VERSION")
    browserstack_build = os.getenv("BROWSERSTACK_BUILD")
    userName = os.getenv("USERNAME1")
    accessKey = os.getenv("ACCESSKEY")
    browserstack_appUrl = os.getenv("BROWSERSTACK_APPURL")
    d = datetime.datetime.now()
    s = d.strftime("%d_%b_%y")
    tag = tag_args.replace('--tags=', '')
    browserstack_build = browserstack_build + "_"+tag+"_" + s
    if tag in ("rerun_ios_clubdeal","rerun_ios_dashboard","rerun_ios_identification","rerun_ios_marketplace","rerun_ios_marketplace_kyc_adequacy","rerun_ios_mydata","rerun_ios_signin","rerun_ios_useraccount"):
        print("Executing in rerun mode")
        # userName = "finexityag1"
        # accessKey = "aCuenAxysq7MGoAEN7LC"

        args = "\"@" + tag + ".txt\"" + f" {report_args}" + f" {output_args}" + " -D browserstack_device=" + f"{browserstack_device}" + " -D device_os_version=" + f"{device_os_version}" + " -D browserstack_build=" + f"{browserstack_build}" + " -D userName=" + f"{userName}" + " -D accessKey=" + f"{accessKey}" + " -D browserstack_appUrl=" + f"{browserstack_appUrl}"

    elif tag in ("ios_clubdeal","ios_dashboard","ios_identification","ios_marketplace","ios_marketplace_kyc_adequacy","ios_mydata","ios_signin","ios_useraccount"):

         log_args = log_args + "rerun_" + tag + ".txt"
         args = log_args +f" {report_args}" + f" {output_args}" +f" {features_args}"+ f" {tag_args}" + f" {skipped_args}" +" -D browserstack_device="+ f"{browserstack_device}"  + " -D device_os_version="+ f"{device_os_version}" + " -D browserstack_build="+ f"{browserstack_build}"+ " -D userName="+ f"{userName}"+ " -D accessKey=" + f"{accessKey}"+ " -D browserstack_appUrl=" + f"{browserstack_appUrl}"

    else:
        log_args="--no-capture"
        args = log_args + f" {report_args}" + f" {output_args}" + f" {features_args}" + f" {tag_args}" + f" {skipped_args}" + " -D browserstack_device=" + f"{browserstack_device}" + " -D device_os_version=" + f"{device_os_version}" + " -D browserstack_build=" + f"{browserstack_build}" + " -D userName=" + f"{userName}" + " -D accessKey=" + f"{accessKey}" + " -D browserstack_appUrl=" + f"{browserstack_appUrl}"


    print(args)

    # store status in file
    # with open('status.pkl', 'wb') as file:
    #     status = True
    #     pickle.dump(status, file)
    #     print(f"Tests to be triggered, status set as TRUE in status.pkl")
    #
    print(f"Argument supplied to behave : {args}")
    testrunner.main(args)
    #
    # # delete file after test execution
    # print(f"Test execution was completed, cleaning up status.pkl")
    # if os.path.isfile("status.pkl"):
    #     os.remove("status.pkl")
    #     print("Cleaned up %s file" % "status.pkl")
    # else:
    #     print("Error: %s file not found" % "status.pkl")


if __name__ == '__main__':
    main()

