import os
import pandas as pd
import xml.etree.ElementTree as ET

# Add the xml file to the root folder
# replace the name of xml_file with your xml file name
xml_file = 'asctt2012.xml'
mytree_isams = ET.parse(xml_file)
mytree_mb = ET.parse(xml_file)
# Define the output file names
mb_name = "timetable-mb.csv"
isams_name = "timetable-isams.csv"
# Week names (when working with two weeks)
# If you are working with more than 2 weeks, find the number system definition within your xml file and replace the lines below
# Adding more weeks would look like this:
# asc_weeks = ['10', '01', '00', ..] <-- not sure if '00' would be correct
# week_array = ['A', 'B', 'C', ..]
asc_weeks = ['10','01']
week_array = ['RW', 'BW']
# Days
# asc_days number system can be found within your xml file
asc_days = ['10000','01000','00100','00010','00001']
day_array = ['Mon','Tue','Wed','Thu','Fri']

home_path = os.path.expanduser('~')
dest_folder = 'Downloads'
isams_file_path = os.path.join(home_path, dest_folder, isams_name)
mb_file_path = os.path.join(home_path, dest_folder, mb_name)

def intr_docs_isams(xml_doc, tag):
    doc_dict = {}

    for xml in xml_doc.iter(tag):
        if tag == 'lesson':
            classids = xml.attrib["classids"]
            teacherids = xml.attrib["teacherids"]
            groupids = xml.attrib["groupids"]

            if ',' in classids:
                array1 = classids.split(",")
                for j in array1:
                    new_element = ET.Element(tag)
                    new_element.set("id",xml.attrib["id"])
                    new_element.set("classids",j)
                    new_element.set("subjectid",xml.attrib["subjectid"])
                    new_element.set("periodspercard",xml.attrib["periodspercard"])
                    new_element.set("periodsperweek",xml.attrib["periodsperweek"])
                    new_element.set("teacherids",xml.attrib["teacherids"])
                    new_element.set("groupids",xml.attrib["groupids"])
                    new_element.set("seminargroup",xml.attrib["seminargroup"])
                    new_element.set("termsdefid",xml.attrib["termsdefid"])
                    new_element.set("weeksdefid",xml.attrib["weeksdefid"])
                    new_element.set("daysdefid",xml.attrib["daysdefid"])
                    new_element.set("capacity",xml.attrib["capacity"])
                    new_element.set("partner_id",xml.attrib["partner_id"])
                
                    xml_doc.append(new_element)

            if ',' in teacherids:
                array2 = teacherids.split(",")
                for k in array2:
                    new_element = ET.Element(tag)
                    new_element.set("id",xml.attrib["id"])
                    new_element.set("classids",xml.attrib["classids"])
                    new_element.set("subjectid",xml.attrib["subjectid"])
                    new_element.set("periodspercard",xml.attrib["periodspercard"])
                    new_element.set("periodsperweek",xml.attrib["periodsperweek"])
                    new_element.set("teacherids",k)
                    new_element.set("groupids",xml.attrib["groupids"])
                    new_element.set("seminargroup",xml.attrib["seminargroup"])
                    new_element.set("termsdefid",xml.attrib["termsdefid"])
                    new_element.set("weeksdefid",xml.attrib["weeksdefid"])
                    new_element.set("daysdefid",xml.attrib["daysdefid"])
                    new_element.set("capacity",xml.attrib["capacity"])
                    new_element.set("partner_id",xml.attrib["partner_id"])
                
                    xml_doc.append(new_element)
            
            if ',' in groupids:
                array3 = groupids.split(",")
                for l in array3:
                    new_element = ET.Element(tag)
                    new_element.set("id",xml.attrib["id"])
                    new_element.set("classids",xml.attrib["classids"])
                    new_element.set("subjectid",xml.attrib["subjectid"])
                    new_element.set("periodspercard",xml.attrib["periodspercard"])
                    new_element.set("periodsperweek",xml.attrib["periodsperweek"])
                    new_element.set("teacherids",xml.attrib["teacherids"])
                    new_element.set("groupids",l)
                    new_element.set("seminargroup",xml.attrib["seminargroup"])
                    new_element.set("termsdefid",xml.attrib["termsdefid"])
                    new_element.set("weeksdefid",xml.attrib["weeksdefid"])
                    new_element.set("daysdefid",xml.attrib["daysdefid"])
                    new_element.set("capacity",xml.attrib["capacity"])
                    new_element.set("partner_id",xml.attrib["partner_id"])
                
                    xml_doc.append(new_element)

            attr = xml.attrib
            doc_dict = attr.copy()
            doc_dict.update(xml.attrib)

            yield doc_dict
        else:
            attr = xml.attrib
            doc_dict = attr.copy()
            doc_dict.update(xml.attrib)

            yield doc_dict

def intr_docs_mb(xml_doc, tag):
    doc_dict = {}

    for xml in xml_doc.iter(tag):
        if tag == 'lesson':
            classids = xml.attrib["classids"]
            if ',' in classids:
                array1 = classids.split(",")
                for j in array1:
                    new_element = ET.Element(tag)
                    new_element.set("id",xml.attrib["id"])
                    new_element.set("classids",j)
                    new_element.set("subjectid",xml.attrib["subjectid"])
                    new_element.set("periodspercard",xml.attrib["periodspercard"])
                    new_element.set("periodsperweek",xml.attrib["periodsperweek"])
                    new_element.set("teacherids",xml.attrib["teacherids"])
                    new_element.set("groupids",xml.attrib["groupids"])
                    new_element.set("seminargroup",xml.attrib["seminargroup"])
                    new_element.set("termsdefid",xml.attrib["termsdefid"])
                    new_element.set("weeksdefid",xml.attrib["weeksdefid"])
                    new_element.set("daysdefid",xml.attrib["daysdefid"])
                    new_element.set("capacity",xml.attrib["capacity"])
                    new_element.set("partner_id",xml.attrib["partner_id"])
                
                    xml_doc.append(new_element)

            attr = xml.attrib
            doc_dict = attr.copy()
            doc_dict.update(xml.attrib)

            yield doc_dict
        else:
            attr = xml.attrib
            doc_dict = attr.copy()
            doc_dict.update(xml.attrib)

            yield doc_dict

def iSAMS_Timetable():
    df_cards = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'card')))
    df_cards.drop('terms',inplace=True,axis=1)

    df_lessons = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'lesson')))
    df_lessons.rename(columns={'id': 'lessonid'},inplace=True, errors='raise')
    df_lessons.drop('periodspercard',inplace=True,axis=1)
    df_lessons.drop('periodsperweek',inplace=True,axis=1)
    #df_lessons.drop('groupids',inplace=True,axis=1)
    df_lessons.drop('termsdefid',inplace=True,axis=1)
    df_lessons.drop('weeksdefid',inplace=True,axis=1)
    df_lessons.drop('daysdefid',inplace=True,axis=1)
    df_lessons.drop('capacity',inplace=True,axis=1)
    df_lessons.drop('partner_id',inplace=True,axis=1)

    df_groups = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'group')))
    df_groups.rename(columns={'id': 'groupids'},inplace=True, errors='raise')
    df_groups.rename(columns={'name': 'groupname'},inplace=True, errors='raise')

    df_classes = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'class')))
    df_classes.rename(columns={'id': 'classids'},inplace=True, errors='raise')
    df_classes.rename(columns={'short': 'set_code'},inplace=True, errors='raise')
    df_classes.drop('teacherid',inplace=True,axis=1)
    #df_classes.drop('grade',inplace=True,axis=1)
    df_classes.drop('partner_id',inplace=True,axis=1)

    df_subjects = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'subject')))
    df_subjects.rename(columns={'id': 'subjectid'},inplace=True, errors='raise')
    df_subjects.rename(columns={'short': 'subjectalias'},inplace=True, errors='raise')
    df_subjects.drop('partner_id',inplace=True,axis=1)

    df_teachers = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'teacher')))
    df_teachers.rename(columns={'id': 'teacherids'},inplace=True, errors='raise')
    df_teachers.drop('name',inplace=True,axis=1)
    df_teachers.drop('firstname',inplace=True,axis=1)
    df_teachers.drop('lastname',inplace=True,axis=1)
    df_teachers.drop('gender',inplace=True,axis=1)
    df_teachers.drop('color',inplace=True,axis=1)
    df_teachers.drop('email',inplace=True,axis=1)
    df_teachers.drop('mobile',inplace=True,axis=1)
    df_teachers.drop('partner_id',inplace=True,axis=1)

    df_rooms = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'classroom')))
    df_rooms.rename(columns={'id': 'classroomids'},inplace=True, errors='raise')
    df_rooms.drop('name',inplace=True,axis=1)
    df_rooms.drop('partner_id',inplace=True,axis=1)

    df_merge_1 = pd.merge(df_lessons, df_subjects, how="left", on="subjectid")
    df_merge_2 = pd.merge(df_merge_1, df_classes, how="left", on="classids")
    #df_merge_2.drop_duplicates(inplace=True)
    df_merge_3 = pd.merge(df_merge_2, df_classes, how="left", on="classids")
    df_merge_4 = pd.merge(df_merge_3, df_teachers, how="left", on="teacherids")
    df_merge_5 = pd.merge(df_merge_4, df_groups, how="left", on="groupids")
    df_merge_6 = pd.merge(df_cards, df_rooms, how="left", on="classroomids")
    df_merge_5.drop('classroomids_y',inplace=True,axis=1)
    df_final = pd.merge(df_merge_6, df_merge_5, how="left", on="lessonid")
    df_final['weeks'] = df_final['weeks'].replace(asc_weeks,week_array)
    df_final['days'] = df_final['days'].replace(asc_days,day_array)
    df_final.rename(columns={'name_x': 'subject'},inplace=True, errors='raise')
    df_final.rename(columns={'name_y': 'class'},inplace=True, errors='raise')
    df_final.rename(columns={'short_x': 'room'},inplace=True, errors='raise')
    df_final.rename(columns={'short_y': 'teacher_initials'},inplace=True, errors='raise')
    df_final.rename(columns={'set_code_x': 'class_code'},inplace=True, errors='raise')
    df_final.rename(columns={'classroomids_x': 'classroomids'},inplace=True, errors='raise')
    df_final.drop('name',inplace=True,axis=1)
    df_final.drop('lessonid',inplace=True,axis=1)
    df_final.drop('buildingid', inplace=True,axis=1)
    df_final.drop('classids',inplace=True,axis=1)
    df_final.drop('subjectid',inplace=True,axis=1)
    df_final.drop('classroomids',inplace=True,axis=1)
    df_final.drop('classroomids_y',inplace=True,axis=1)
    df_final.drop('classid',inplace=True,axis=1)
    df_final.drop('studentids',inplace=True,axis=1)
    df_final.drop('entireclass',inplace=True,axis=1)
    df_final.drop('grade_x',inplace=True,axis=1)
    df_final.drop('grade_y',inplace=True,axis=1)
    df_final.drop('set_code_y',inplace=True,axis=1)
    df_final = df_final[df_final['groupids'].str.len() < 17]
    df_final = df_final[df_final['teacherids'].str.len() < 17]
    df_final.drop('groupids',inplace=True,axis=1)
    df_final.drop('teacherids',inplace=True,axis=1)
    df_final.drop_duplicates(inplace=True)
    df_final = df_final[df_final['class'].notna()]

    df_final.to_csv(isams_file_path)

def MB_Timetable():
    df_cards = pd.DataFrame(list(intr_docs_mb(mytree_mb.getroot(), 'card')))
    df_cards.drop('terms',inplace=True,axis=1)

    df_lessons = pd.DataFrame(list(intr_docs_mb(mytree_mb.getroot(), 'lesson')))
    df_lessons.rename(columns={'id': 'lessonid'},inplace=True, errors='raise')
    df_lessons.drop('periodspercard',inplace=True,axis=1)
    df_lessons.drop('periodsperweek',inplace=True,axis=1)
    #df_lessons.drop('groupids',inplace=True,axis=1)
    df_lessons.drop('termsdefid',inplace=True,axis=1)
    df_lessons.drop('weeksdefid',inplace=True,axis=1)
    df_lessons.drop('daysdefid',inplace=True,axis=1)
    df_lessons.drop('capacity',inplace=True,axis=1)
    df_lessons.drop('partner_id',inplace=True,axis=1)

    df_groups = pd.DataFrame(list(intr_docs_isams(mytree_isams.getroot(), 'group')))
    df_groups.rename(columns={'id': 'groupids'},inplace=True, errors='raise')
    df_groups.rename(columns={'name': 'groupname'},inplace=True, errors='raise')

    df_classes = pd.DataFrame(list(intr_docs_mb(mytree_mb.getroot(), 'class')))
    df_classes.rename(columns={'id': 'classids'},inplace=True, errors='raise')
    #df_classes.drop('short',inplace=True,axis=1)
    df_classes.drop('teacherid',inplace=True,axis=1)
    #df_classes.drop('grade',inplace=True,axis=1)
    df_classes.drop('partner_id',inplace=True,axis=1)

    df_subjects = pd.DataFrame(list(intr_docs_mb(mytree_mb.getroot(), 'subject')))
    df_subjects.rename(columns={'id': 'subjectid'},inplace=True, errors='raise')
    df_subjects.rename(columns={'short': 'subjectalias'},inplace=True, errors='raise')
    df_subjects.drop('partner_id',inplace=True,axis=1)

    df_teachers = pd.DataFrame(list(intr_docs_mb(mytree_mb.getroot(), 'teacher')))
    df_teachers.rename(columns={'id': 'teacherids'},inplace=True, errors='raise')
    df_teachers.drop('name',inplace=True,axis=1)
    df_teachers.drop('firstname',inplace=True,axis=1)
    df_teachers.drop('lastname',inplace=True,axis=1)
    df_teachers.drop('gender',inplace=True,axis=1)
    df_teachers.drop('color',inplace=True,axis=1)
    df_teachers.drop('email',inplace=True,axis=1)
    df_teachers.drop('mobile',inplace=True,axis=1)
    df_teachers.drop('partner_id',inplace=True,axis=1)

    df_rooms = pd.DataFrame(list(intr_docs_mb(mytree_mb.getroot(), 'classroom')))
    df_rooms.rename(columns={'id': 'classroomids'},inplace=True, errors='raise')
    df_rooms.drop('name',inplace=True,axis=1)
    df_rooms.drop('partner_id',inplace=True,axis=1)

    df_merge_1 = pd.merge(df_lessons, df_subjects, how="left", on="subjectid")
    df_merge_2 = pd.merge(df_merge_1, df_classes, how="left", on="classids")
    df_merge_3 = pd.merge(df_merge_2, df_classes, how="left", on="classids")
    df_merge_4 = pd.merge(df_merge_3, df_teachers, how="left", on="teacherids")
    df_merge_5 = pd.merge(df_merge_4, df_groups, how="left", on="groupids")
    df_merge_5.drop('classroomids_y',inplace=True,axis=1)
    df_merge_5.drop('short_y',inplace=True,axis=1)
    df_merge_6 = pd.merge(df_cards, df_rooms, how="left", on="classroomids")
    df_final = pd.merge(df_merge_6, df_merge_5, how="left", on="lessonid")
    df_final['weeks'] = df_final['weeks'].replace(asc_weeks,week_array)
    df_final['days'] = df_final['days'].replace(asc_days,day_array)
    df_final.rename(columns={'name_x': 'subject'},inplace=True, errors='raise')
    df_final.rename(columns={'name_y': 'class'},inplace=True, errors='raise')
    df_final.rename(columns={'short_x': 'room'},inplace=True, errors='raise')
    df_final.rename(columns={'short_y': 'initials'},inplace=True, errors='raise')
    df_final.rename(columns={'classroomids_x': 'classroomids'},inplace=True, errors='raise')
    df_final.drop('name',inplace=True,axis=1)
    df_final.drop('lessonid',inplace=True,axis=1)
    df_final.drop('classids',inplace=True,axis=1)
    df_final.drop('subjectid',inplace=True,axis=1)
    df_final.drop('classroomids',inplace=True,axis=1)
    df_final.drop('classroomids_y',inplace=True,axis=1)
    df_final.drop('classid',inplace=True,axis=1)
    df_final.drop('studentids',inplace=True,axis=1)
    df_final.drop('entireclass',inplace=True,axis=1)
    df_final = df_final[df_final['class'].notna()]

    df_final.to_csv(mb_file_path)

iSAMS_Timetable()
MB_Timetable()