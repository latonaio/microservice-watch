import sys
import os
import traceback

from aion.microservice import main_decorator, Options
from aion.logger import initialize_logger, lprint
from src.template_matching_summary import TemplateMatchingSummaryWatch

SERVICE_NAME = os.environ.get("SERVICE")
CURRENT_DEVICE_NAME = os.environ.get("CURRENT_DEVICE_NAME")
NEXT_DEVICE_NAME = os.environ.get("NEXT_DEVICE_NAME")

initialize_logger(SERVICE_NAME)


@main_decorator(SERVICE_NAME)
def main(opt: Options):
    conn = opt.get_conn()
    num = opt.get_number()

    try:
        for kanban in conn.get_kanban_itr(SERVICE_NAME, num):
            metadata = kanban.get_metadata()
            template_matching_summary = metadata['TemplateMatchingSummary']

            if CURRENT_DEVICE_NAME in ["deneb", "elpis", "moca"]:
                t = TemplateMatchingSummaryWatch("trigger")
                t.print_template_matching(template_matching_summary)
            elif CURRENT_DEVICE_NAME in ["lib", "neo", "poseidon", "tartarus"]:
                t = TemplateMatchingSummaryWatch("vehicle")
                t.print_template_matching(template_matching_summary)

                if template_matching_summary['end']['status']:
                    templates = metadata["TemplateMatchingSetTemplates"]
                    if NEXT_DEVICE_NAME:
                        conn.output_kanban(
                            result=True,
                            connection_key="default",
                            metadata=templates,
                            device_name=NEXT_DEVICE_NAME,
                        )
                        lprint(f"output_kanban to other device {NEXT_DEVICE_NAME} {templates}")
                    else:
                        lprint("next_device_name is none")

    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
